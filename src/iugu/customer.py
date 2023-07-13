from datetime import datetime

class CustomerActions:

    #from iugu import Iugu

    def __init__(self, iugu) -> None:
        
        self.iugu = iugu

        self.endpoint = '/customers'

    def create(self, 
               email: str,
               name: str,
               notes: str = None,
               phone: int = None,
               phone_prefix: str = None,
               cpf_cnpj: str = None,
               cc_emails: str = None,
               zip_code: str = None,
               number: str = None,
               street: str = None,
               city: str = None,
               state: str = None,
               district: str = None,
               complement: str = None,
            ):
        
        payload = {
            'email':        email,
            'name':         name,
            'notes':        notes,
            'phone':        phone,
            'phone_prefix': phone_prefix,
            'cpf_cnpj':     cpf_cnpj,
            'cc_emails':    cc_emails,
            'zip_code':     zip_code,
            'number':       number,
            'street':       street,
            'city':         city,
            'state':        state,
            'district':     district,
            'complement':   complement,
        }
        
        new_customer = self.iugu.request(
                            method = 'POST',
                            url = self.endpoint,
                            json = payload
                        )
        
        return new_customer
        
    def list(self, 
             limit: int = 100,
             start: int = 0,
             created_at_from: datetime = None,
             created_at_to: datetime = None,
             updated_since: datetime = None,
             query: str = None
            ):
        
        query_params = {
            'limit': limit,
            'start': start,
            'created_at_from': created_at_from,
            'created_at_to': created_at_to,
            'updated_since': updated_since,
            'query': query
        }
        
        customers = self.iugu.request(
                            method = 'GET',
                            url = self.endpoint,
                            params = query_params
                        )
        
        return customers
