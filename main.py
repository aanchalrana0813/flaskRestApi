from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/armstrong/<int:n>')
def armstrong(n):
  n = int(input("Enter the number\n"))
  sum = 0
  order = len(str(n))
  copy_n = n
  while(n>0):
    digit = n%10
    sum += digit ** order
    n = n/10

  if(sum == copy_n):
    print(f"{copy_n} is a Armstrong Number")
    return "True"
  else:
    print(f"{copy_n} is not a Armstrong Number")
    return "False"

if __name__ == "__main__":
  app.run(debug=True)