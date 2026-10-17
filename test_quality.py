import unittest
import pandas as pd
from quality import select
class Gate(unittest.TestCase):
 def test_membership_and_copy(self):
  frame=pd.DataFrame({'asin':['a','b','c','d','e'],'title':['valid','  ',None,'low','valid'],'price':[10,20,30,40,None],'average_rating':[4.8,5,5,4.2,5]})
  before=frame.copy(deep=True);self.assertEqual(select(frame).asin.tolist(),['a']);pd.testing.assert_frame_equal(frame,before)
 def test_invalid(self):
  good=pd.DataFrame({'asin':['a'],'title':['valid'],'price':[10],'average_rating':[4.8]})
  for field,value in [('price',-1),('average_rating',6),('asin',None)]:
   bad=good.copy();bad[field]=value
   with self.assertRaises(ValueError):select(bad)
  with self.assertRaises(ValueError):select(pd.concat([good,good]))
  with self.assertRaises(ValueError):select(good.drop(columns='price'))
if __name__=='__main__':unittest.main()
