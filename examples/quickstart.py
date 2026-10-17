"""Offline example using the public implementation; see README for evidence scope."""
import sys,json,pathlib,os
repo=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(repo));sys.path.insert(0,str(repo/'src'));os.chdir(repo)
import ast,pandas as pd
nb=json.loads((repo/'analysis.ipynb').read_text());scope={'pd':pd}
for cell in nb['cells']:
 if cell['cell_type']!='code':continue
 tree=ast.parse(''.join(cell['source']))
 for node in tree.body:
  if isinstance(node,ast.FunctionDef) and node.name in ['get_product','calculate_percentage']:exec(compile(ast.Module(body=[node],type_ignores=[]),'analysis.ipynb','exec'),scope)
raw=pd.DataFrame({'asin':['A','B'],'title':['Headphones','Speaker'],'price':[99.,None],'average_rating':[4.8,4.9]})
print(json.dumps({"fixture":"two generated product records","known":scope['get_product']('A',raw),"missing_price":scope['get_product']('B',raw),"unknown":scope['get_product']('Z',raw),"retained_one_of_two_percent":scope['calculate_percentage'](1,2)}))
