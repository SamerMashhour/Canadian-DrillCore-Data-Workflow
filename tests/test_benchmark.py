import pandas as pd
from drillcore_workflow.benchmark import leave_one_group_out_splits, evaluate_whole_group_baselines


def test_whole_hole_splits_have_no_group_overlap():
    df = pd.DataFrame({"hole_id":["A","A","B","B"], "x":[0,1,2,3], "label":[0,0,1,1]})
    for held, train, test in leave_one_group_out_splits(df, "hole_id"):
        assert set(df.loc[train,"hole_id"]) & set(df.loc[test,"hole_id"]) == set()


def test_baselines_execute_on_two_group_demo():
    rows=[]
    for hole, shift in [("A",0.0),("B",0.2)]:
        for i in range(12):
            label = 0 if i < 6 else 1
            rows.append({"hole_id":hole,"f1":label+shift+i*0.001,"f2":label*2+shift,"label":label})
    df=pd.DataFrame(rows)
    out=evaluate_whole_group_baselines(df,["f1","f2"],"label","hole_id")
    assert {x["model"] for x in out} == {"dummy_prior","logistic_balanced","random_forest_balanced"}
