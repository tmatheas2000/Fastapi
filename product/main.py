from fastapi import FastAPI
from .import models
from .database import engine
from .routes import product, seller, login

app = FastAPI(title='Product API', 
              description="Get details for all the products on our website", 
              terms_of_service="https://matheas-portfolio.web.app/", 
              contact={
                  "Developer Name": "Matheas T",
                  "website": "https://matheas-portfolio.web.app/",
                  "email": "tmatheas@gmail.com"
                },
              license_info={
                  "name": "License",
                  "url": "https://google.com"
                },
              )

app.include_router(login.router)
app.include_router(product.router)
app.include_router(seller.router)

models.Base.metadata.create_all(engine)