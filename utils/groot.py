'''
I am Groot Programme

Print the title

Render the gif
'''

print("I am Groot")


from IPython.display import Image
#Image(url='groot.gif')

'''
'<img src="groot.gif">'

from IPython.display import HTML
HTML('<img src="groot.gif">')
'''

with open('utils/groot.gif','rb') as f:
    display(Image(data=f.read(), format='png', width=217, height=333))

