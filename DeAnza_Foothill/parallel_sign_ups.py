from DeAnza_Foothill.DeAnza_and_Foothill import FHDA_ClassSignUp
import threading
import pandas as pd


def registration_call():
    id = student_ids[student_count]
    password = passwords[student_count]
    CRNs = _CRNs[student_count]
    term = terms[student_count]
    my_sign_up = FHDA_ClassSignUp(id, password, De_Anza=True, Foothill=False, term=term
                                  , CRNs=CRNs)
    my_sign_up.sign_up_for_my_classes()


student_count = 0
df = pd.read_csv('example_text_file.txt')
student_ids = df['student_id'].tolist()
passwords = df['password'].tolist()
terms = df['term'].tolist()
_CRNs = df['CRNs'].tolist()
for i in range(len(_CRNs)):
    _CRNs[i] = _CRNs[i].split()

thread_list = list()
# can create as much as we want, just did 2 for testing
for i in range(2):
    t = threading.Thread(name='Test {}'.format(i), target=registration_call)
    t.start()
    thread_list.append(t)
    student_count += 1

for thread in thread_list:
    thread.join()
