#from ..xplain import Xsession, Query_config
import xplain
from setting import (URL, USER, PASSWORD, TESTSET, SESSIONID)
import secrets
from apiQueries import apiQueries
import jsondiff
from pathlib import Path
from references.BTS1 import apiQueryOutput

def test_BTS1WebapiAddAggregation():
    s1 = xplain.Xsession(URL, USER, PASSWORD)

    s1.startup(TESTSET)

    for i in range(len(apiQueries)):
        df1 = s1.execute_query(apiQueries[i]).T.reset_index(drop=True).to_json(orient="split")
        print(i, df1)
        #print(i, df1, i, apiQueryOutput[i], jsondiff.diff(apiQueryOutput[i], df1))
        #assert len(jsondiff.diff((apiQueryOutput[i]), df1)) == 0


    assert False

    s1.terminate()