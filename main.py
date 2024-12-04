from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - maut123-coll-057e3731199143ecac80500e418cea8b',debug=False,docs_url='/priceless-antonelli-e7b05a6eac8d11efa0260242ac12000287/docs',openapi_url='/priceless-antonelli-e7b05a6eac8d11efa0260242ac12000287/openapi.json')

app.include_router(router, prefix='/priceless-antonelli-e7b05a6eac8d11efa0260242ac12000287/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()