#Project 1
#NAME(S): Gaby Ackermann Logan and Tara Donohue
#HOURS SPENT: 1
path = "/Users/gackermannlogan/Documents/Github/project-1-gaby-tara/Step/3"
import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=6, length =100)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)


# Wait for start message before beginning printing
incoming = ''
while not incoming == 'start':
    incoming = radio.receive()
print('start')


while True:
    incoming = radio.receive() # Read from radio

    if incoming is not None: # message was received
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False)
        tuple(incoming)
        print(incoming)

        mb.sleep(10)
