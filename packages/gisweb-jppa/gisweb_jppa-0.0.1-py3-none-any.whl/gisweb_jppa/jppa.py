
# type: ignore
from calendar import c
from typing import Any
from gisweb_jppa.schema import IConfigPagoPa, IDebito, IImporto, ISoggetto, IDataPagoPa, ITipoEnum, IEsito, IChiaveDebito
import logging
import os, base64, uuid
import json
from datetime import datetime, date
from pydantic import BaseModel
from jinja2 import Environment, PackageLoader, select_autoescape
import time
import httpx
from bs4 import BeautifulSoup
import base64


_logger = logging.getLogger('gisweb-jppa')


env = Environment(
    loader=PackageLoader("gisweb_jppa"),
    autoescape=select_autoescape()
)

class Jppa:
    
    config:IConfigPagoPa
  
    def __init__(self, config:IConfigPagoPa):
        self.config = config
        
    async def pagamentoImmediato(self, soggetto: ISoggetto, debito: IDebito, testXml:bool=True):
        
        config  = self.config
        
        template = env.get_template("Soggetto.xml")
        xml_soggetto = template.render(soggetto)
                
        template = env.get_template("Debito.xml")
        context = debito.model_copy(update=dict(soggetto=xml_soggetto))
        xml_debito = template.render(context)
        
        template = env.get_template("PagaDebiti.xml")
        context = dict(
            idPagamento=debito.iddeb,###boh...
            soggetto=xml_soggetto,
            debito=xml_debito,
            notifica_ok=config.notificaOK, 
            notifica_ko=config.notificaKO, 
            notifica_pagamento=config.notificaPagamento,
        )
        
        xml_paga_debiti = template.render(context)
        
        if testXml:
            return xml_paga_debiti
        
        result = await self.serviceCall(Operazione="PagaDebiti", xml = xml_paga_debiti)
        
        return result

        
        

        
        
    
    async def infoPagamento(self, deb:IChiaveDebito):
        template = env.get_template("InfoPagamentoDebito.xml")
        xml = template.render(deb)
        return await self.serviceCall(Operazione='InfoPagamentoDebito',xml=xml, testXml=False)


    async def setPagamento(self, deb:IChiaveDebito):
        template = env.get_template("InfoPagamentoDebito.xml")
        xml = template.render(deb)
        data = self.serviceCall(Operazione='InfoPagamentoDebito',xml=xml, testXml=False)
        #res = crud.pagamenti.aggiorna_pagamento(data=data)
    
    
        
    
    async def serviceCall(self, Operazione:str, xml:str):# -> IEsito:
        """
        chiamata base al servizio JPPA
        """
        
        config = self.config
        data_richiesta =  datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ') 

        template = env.get_template("serviceCall.xml")
        xml = template.render(
            operazione=Operazione, 
            content=xml, 
            data=data_richiesta, 
            codice_ipa=config.codiceIpa, 
            codice_servizio=config.codiceServizio
        )
        
        headers={'Content-type': 'text/plain; charset=utf-8'}
                
        async with httpx.AsyncClient() as client:
            
            #import pdb;pdb.set_trace()
            print(xml)
            
            response = await client.post(config.wsUrl, content=xml, headers=headers)
            soup = BeautifulSoup(response.text, 'xml')
            
            if soup.find('EsitoOperazione') and soup.find('DatiDettaglioRisposta'):
                if soup.find('EsitoOperazione').string == "OK":
                    return await self.parseResponse(soup.find('DatiDettaglioRisposta').string)
                elif soup.find('EsitoOperazione').string == "ERROR":
                    try:
                        return {"esito":soup.find('EsitoOperazione').string, "errore":soup.find('Codice').string, "descrizione":soup.find('Descrizione').string}
                    except:
                        with open("./jppa_resp.xml", "a") as f:
                            f.write(response.text)

                    
            else:
                with open("./jppa_resp.xml", "a") as f:
                    f.write(response.text)
   
        return {"esito":"ERRORE NON GESTITO"}

                        
                
                
    async def parseResponse(self, xml:str) -> IEsito:
        
        #import pdb;pdb.set_trace()
        soup = BeautifulSoup(xml, 'xml')
        esito = soup.find("Esito")
        url = soup.find("Url") and soup.find("Url").string
        if soup.find("ChiaveDebito"):
            chiave = soup.find("ChiaveDebito") and soup.find("ChiaveDebito").string
        if soup.find("IdentTransazione"):
            chiave = soup.find("IdentTransazione") and soup.find("IdentTransazione").string
        avviso = soup.find("NumeroAvviso") and soup.find("NumeroAvviso").string

        #la struttura è nidificata...esito->esito
        if esito:
            stresito = esito.find('Esito') and esito.find('Esito').string
            if stresito == 'OK':
                return {"esito":stresito, "chiave":chiave, "url":url, "avviso":avviso}
            elif stresito == 'Error':
                if esito.find('Messaggio') :
                    return {"esito":stresito, "errore":esito.find('Messaggio').string}
                
        #nel caso di EliminaAvvisoPagamento non mette esito!!!
        elif avviso:
            return {"esito":"OK", "avviso":avviso}
                
        with open("./jppa_resp.xml", "a") as f:
            f.write(xml)
        return {"esito":"ERRORE NON GESTITO"}
    
    async def stampaAvvisoPagamento(self):
        
        with open("logo.png", "rb") as f:
            logo = base64.b64encode(f.read()).decode("latin1")
        
        xx=dict(
            codiceIpaEnte=self.config.codiceIpa,
            codiceServizio=self.config.codiceServizio,
            codiceTipoDebito=self.data.debito.codice,
            idDebito=self.data.debito.iddeb,
            idPosizione=self.data.debito.idpos,
        )
        
        data = dict(
            authKeyDto = dict(username=self.config.wsUser,password=self.config.wsPassword),
            base64FileLogoEnte = logo,
            numeroAvviso = self.data.debito.iuv,
            testoInformativaCanaliDigitali="ff sf asdf asdf asd fasdf asd f",
            chiaviDebito=xx
        )
        
        with httpx.AsyncClient() as client:
            response =  client.post(self.config.wsPrintUrl, data = json.dumps(data), headers = {'Content-type': 'application/json; charset=utf-8'})
            if response.status_code == httpx.codes.OK:
                try:
                    return response.json()
                except:
                    return {"errore":"SSSSSSSSSSSS"}
            else:
                return {"errore":"SSSSSSSSSSSS"}
        

    
    
    

    async def provaXML(self):
        respOK='''
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <PagaDebitiResponse xmlns="http://schemi.informatica.maggioli.it/ws/pagopa/ServiziInterni">
            <CodiceIPA>c_h183</CodiceIPA>
            <IDOperazione>PagaDebiti</IDOperazione>
            <DataRisposta>2024-04-03T12:52:27.499+02:00</DataRisposta>
            <EsitoOperazionedd>OK</EsitoOperazione>
            <DatiDettaglioRisposta>&lt;RispostaPagaDebiti xmlns="http://schemi.informatica.maggioli.it/operations/jcgpagopa/1_2">
    &lt;Url>https://pspagopa.comune-online.it/jcitygov-pagopa/web/webpagopa/pagaCarrello?identTransazione=9c03ce84-c46b-4771-a763-f6298093100e&amp;amp;token=427212cb-671b-4b37-8529-318e6503facd&lt;/Url>
    &lt;IdentTransazione>9c03ce84-c46b-4771-a763-f6298093100e&lt;/IdentTransazione>
    &lt;Esito>
        &lt;Esito>OK&lt;/Esito>
    &lt;/Esito>
&lt;/RispostaPagaDebiti></DatiDettaglioRisposta>
        </PagaDebitiResponse>
    </soap:Body>
</soap:Envelope>
        '''
        
        respERRORE='''
        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <PagaDebitiResponse xmlns="http://schemi.informatica.maggioli.it/ws/pagopa/ServiziInterni">
            <CodiceIPA>c_h183</CodiceIPA>
            <IDOperazione>PagaDebiti</IDOperazione>
            <DataRisposta>2024-04-03T13:29:30.775+02:00</DataRisposta>
            <EsitoOperazione>OK</EsitoOperazione>
            <DatiDettaglioRisposta>&lt;RispostaPagaDebiti xmlns="http://schemi.informatica.maggioli.it/operations/jcgpagopa/1_2">
    &lt;Url>https://pspagopa.comune-online.it/jcitygov-pagopa/web/webpagopa/pagaCarrello?identTransazione=ND&amp;amp;token=e83df496-7752-4ba6-a594-3a0e3fbb471e&lt;/Url>
    &lt;IdentTransazione>ND&lt;/IdentTransazione>
    &lt;Esito>
        &lt;Esito>Error&lt;/Esito>
        &lt;Messaggio>[I193_ERR_DATI_ACCERTAMENTO_INCONSISTENTI] I dati di accertamento non sono coerenti. Verificare che la somma degli importi specificati nell'oggetto &amp;lt;DettagliImporto&amp;gt; coincida con il valore dell'importo specificato nell'oggetto &amp;lt;DettaglioDebito&amp;gt;.&lt;/Messaggio>
    &lt;/Esito>
&lt;/RispostaPagaDebiti></DatiDettaglioRisposta>
        </PagaDebitiResponse>
    </soap:Body>
</soap:Envelope>
        '''
        
        import pdb;pdb.set_trace()
        Operazione = "PagaDebiti"
        soup = BeautifulSoup(respOK, 'xml')
        esito = soup.find("EsitoOperazione") and soup.find("EsitoOperazione").string
        if esito == 'OK':
            respXml = soup.find('DatiDettaglioRisposta').string
            soupresp = BeautifulSoup(respXml, 'xml')
            print(soupresp)
        elif esito == 'ERROR':
            print('ddddddd')
            
        
           

                
        
                


        
         
  




