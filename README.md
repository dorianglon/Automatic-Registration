# Automatic-Registration
automatic sign up for classes

## Usage

```python
from DeAnza_Foothill.DeAnza_and_Foothill import FHDA_ClassSignUp

# create list with CRN for classes you want to sign up for
CRNs = ['CRN_number1', 'CRN_number2']

# create instance of sign up class and provide student id, password, deanza or foothill bool, term, and CRNs
my_sign_up = FHDA_ClassSignUp('student_id', 'password', De_Anza=True, Foothill=False, term='summer'
                              , CRNs=CRNs)
                              
# sign up for classes                           
my_sign_up.sign_up_for_my_classes()
```
