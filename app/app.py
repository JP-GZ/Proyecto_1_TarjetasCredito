from fastapi import FastAPI
from models.request_evaluation import RequestEvaluation
import pandas as pd
from models.amortization import *

app = FastAPI()

# with open('../models/model.pkl','rb') as file:
#     model = pickle.load(file, encoding='latin1')
model = pd.read_pickle(open('./models/model.pkl', 'rb'))


@app.get("/health")
def checkhealt():
    return {"isalive": True}


@app.post("/evaluate")
async def evaluate(req: RequestEvaluation):
    print(req)
    df = pd.DataFrame({
        "int_rate": [req.int_rate],
        "out_prncp": [req.out_prncp],
        "total_rec_prncp": [req.total_rec_prncp],
        "last_pymnt_amnt": [req.last_pymnt_amnt],
        "addr_state": [req.addr_state],
        "grade": [req.grade],
        "sub_grade": [req.sub_grade],
        "total_pymnt": [req.total_pymnt],
    })
    pred = model.predict_proba(df)[0]
    default_prob = pred[1]
    print(default_prob)
    amort = Amortization(100_000, 0.5, 12, default_prob)
    opt_rate = Amortization.optimize_expected_irr(0, amort)
    return dict(pd=f"{default_prob * 100:.2f} %", interest_rate=f"{opt_rate * 100:.4f} %")

# comand uvicorn app.app:app --reload --port 8899

# en postamn/ headers poner json y en body poner el json con la informacion


# dentro de utils ponemos la clase de amortizacion
