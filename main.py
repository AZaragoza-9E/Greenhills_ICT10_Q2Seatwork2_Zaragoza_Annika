from pyscript import display, document



def gradecalculator(e):
    document.getElementById('results').innerHTML = ""

    firstname = document.getElementById('firstname').value
    lastname = document.getElementById('lastname').value
    name = f'{firstname} {lastname}'

    display(f'Student Name: {name}', target='results')

    science = document.getElementById('science').value
    english = document.getElementById('english').value
    filipino = document.getElementById('filipino').value
    mathematics = document.getElementById('mathematics').value
    ss = document.getElementById('ss').value
    ve = document.getElementById('ve').value

    display(f'Science: {science}', target='results')
    display(f'English: {english}', target='results')
    display(f'Filipino: {filipino}', target='results')
    display(f'Mathematics: {mathematics}', target='results')
    display(f'SS: {ss}', target='results')
    display(f'VE: {ve}', target='results')

    #i asked my dad how to properly work the float stuff so this code is a mix of his code and the exercises
    science = int(("") or 0)
    english = int(("") or 0)
    filipino = int(("") or 0)
    mathematics = int(("") or 0)
    ss = int(("") or 0)
    ve = int(("") or 0)

    subjects = [science, english, filipino, mathematics, ss, ve] 
    units = (5, 3, 2) 


    final = round((float(subjects[0]) * units[0] +
        float(subjects[1]) * units[0] +
        float(subjects[2]) * units[1] +
        float(subjects[3]) * units[0] +
        float(subjects[4]) * units[1] +
        float(subjects[5]) * units[2]) / 
        (units[0] + units[0] + units[1] + units[0] + units[1] + units[2]), 2)

    display(f' Your Weighted Average: {final}', target='results')
