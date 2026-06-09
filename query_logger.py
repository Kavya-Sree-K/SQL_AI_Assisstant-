import pandas as pd
from datetime import datetime
import os

LOG_FILE = "logs/queries.csv"

def log_query(question, answer):

    # Create logs folder if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    data = {
        "Timestamp": [datetime.now()],
        "Question": [question],
        "Answer": [str(answer)]
    }

    df = pd.DataFrame(data)

    if os.path.exists(LOG_FILE):
        df.to_csv(
            LOG_FILE,
            mode="a",
            header=False,
            index=False
        )
    else:
        df.to_csv(
            LOG_FILE,
            index=False
        )