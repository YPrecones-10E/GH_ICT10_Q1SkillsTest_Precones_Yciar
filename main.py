# Defining Variables
from pyscript import display, document

def order(e):
    document.getElementById('cont').innerHTML=""
    item1=document.getElementById('menu1')
    item2=document.getElementById('menu2')
    item3=document.getElementById('menu3')
    item4=document.getElementById('menu4')
    item5=document.getElementById('menu5')
    
    total = (float(item1.value) * item1.checked +
    float(item2.value) * item2.checked +
    float(item3.value) * item3.checked +
    float(item4.value) * item4.checked +
    float(item5.value) * item5.checked)

    name = document.getElementById('name').value
    address = document.getElementById('address').value
    contact = document.getElementById('contact').value

    summary = f"""Order Summary
    Your total is P{total}.
    Name : {name}
    Address : {address}
    Contact : {contact}
    """

    display(f'{summary}', target='cont')