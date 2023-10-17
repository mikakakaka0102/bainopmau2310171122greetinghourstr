#region debai
"""
--- ma debai / id
greeting(hour_str)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/bainopmau2310171122greetinghourstr

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/mb6ZrFw4pXW8DqeBA

--- debai / problem
Viết hàm 
  greeting(hour_str)
giúp chat bot in ra câu chào theo buổi sáng/chiều/tối trong ngày 
00:00AM  - 11:59AM Good morning!
12:00PM  - 05:59PM Good afternoon!
06:00PM  - 11:59PM Good evening!

Khi chạy với đầuvào / input  | Kếtquả đẩura / output  | Thứtự mẫuthử 
---------------------------- | ---------------------- | -----------
greeting(hour_str='6am')     | Good morning!          | 00

# AM / PM format
greeting('6am')              | Good morning!          | 01
greeting('6 am')             | Good morning!          | 02
greeting('6AM')              | Good morning!          | 03
greeting('6 AM')             | Good morning!          | 04

greeting('9pm')              | Good evening!          | 05
greeting('0900pm')           | Good evening!          | 06
greeting('09:00pm')          | Good evening!          | 07
greeting('09:00 pm')         | Good evening!          | 08
greeting('09:00 PM')         | Good evening!          | 09

greeting('1pm')              | Good afternoon!        | 10

# 24-hours format
greeting('06:00')            | Good morning!          | 11
greeting('0600')             | Good morning!          | 12
greeting('21:00')            | Good evening!          | 13
greeting('2100')             | Good evening!          | 14

"""
#endregion debai
#region bailam
def greeting(hour_str):
  s=hour_str.lower()
  #print(hour_str)
  tem=0
  if 'am' or 'pm' in s:
    for i in range(0,len(s)):
      if(s[i]=='p'):
         tem+=1
         break
    if(tem==1):
      if ':' in s:
        a=s.split(':')[0]
      else:
        a=str(s.split('pm')[0])
        if len(a)>2:
          a=a[:2]
      a=str(int(a)+12)
    else:
      a=s.split('am')[0]  
  else:
    if ":"in s:
      a=str(int(s.split(':')[0]))
    else:
      a=str(int(s.split('0')[0]))
  temp=""
  i=0
  while(len(temp)<2):
    if i== len(a):
      break
    if a[i]!='0' or a[i]!='':
      temp+=a[i]
    
    i+=1
  #ans = ""
  temp=int(temp)
  if(temp>24):
    while(True):
        if(temp%10==0):
            temp= temp/ 10
        else:
            break
  if temp<12 or temp==24:
    return 'Good morning!'
  if temp<18 and temp>=12:
    return "Good afternoon!"
  if temp<24 and temp>=18:
    return "Good evening!"
#endregion bailam
