from fastapi import FASTAPI, BackgroundTasks
from pydantic import BaseModel, Validator

#initialize web app
app = FastAPI()

class Translation (BaseModel):
    text : str
    base_lang : str
    final_lang : str

    Languages = ["English", "French", "Roman"]
    @validator ('base_lang', 'final_lang')
    def valid_lang (cls, lang):
        if lang not in languages:
            raise ValueError ("Invalid language")
        return lang
#Route 1: / It's the index route
#Test if everything is working
@app.get("/") #It's the base of the server in the Webapp
def get_root():
    return {"hello world"}

# Note : get is used when asking the server for some data
# and push request when pushing some data to the server to be processed

