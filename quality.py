"""Reusable product gate with explicit schema and numeric contracts."""
import argparse,hashlib,json
from pathlib import Path
import pandas as pd,numpy as np

def select(frame,minimum_rating=4.5):
 if not 0<=minimum_rating<=5:raise ValueError('Rating threshold must be within0..5')
 required={'asin','title','average_rating','price'}
 if required-set(frame):raise ValueError('Missing product columns: '+', '.join(sorted(required-set(frame))))
 if frame.asin.isna().any() or frame.asin.duplicated().any():raise ValueError('Nonmissing unique ASIN required')
 result=frame.copy();rating=pd.to_numeric(result.average_rating,errors='coerce');price=pd.to_numeric(result.price,errors='coerce')
 if np.isinf(rating).any() or np.isinf(price).any() or ((rating<0)|(rating>5)).any() or (price<0).any():raise ValueError('Invalid price or rating')
 keep=result.title.notna()&result.title.astype(str).str.strip().ne('')&rating.ge(minimum_rating)&price.notna()
 result['average_rating']=rating;result['price']=price
 return result.loc[keep].copy()
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('csv',type=Path);p.add_argument('--output',type=Path,required=True);p.add_argument('--minimum-rating',type=float,default=4.5);a=p.parse_args()
 if a.output.exists():raise ValueError('Use a new output directory')
 a.output.mkdir(parents=True);frame=pd.read_csv(a.csv);result=select(frame,a.minimum_rating);result.to_csv(a.output/'selected.csv',index=False)
 (a.output/'metrics.json').write_text(json.dumps({'input_sha256':hashlib.sha256(a.csv.read_bytes()).hexdigest(),'input_rows':len(frame),'selected_rows':len(result),'minimum_rating':a.minimum_rating},indent=2)+'\n')
