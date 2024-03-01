

class Reader:
    def from_terminal():
      return input('Введите что-нибудь: ')

class Send:
  def to_terminal(msg):
      print(f'Послали в терминал: {msg}')


  def send_message(msg):
      print(f"Послали по сети: {msg}")

class process:
  def process(from_file=False, send_to=False):
      if from_file:
          msg = file_read()
      else:
          msg = from_terminal()
          if send_to:
              send_message(msg)
          else:
              to_terminal(msg)


process()
process(True)
process(True, True)
process(False, True)
