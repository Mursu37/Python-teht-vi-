from flask import Flask
# import json
app = Flask(__name__)


@app.route("/alkuluku/<int:number>")
def prime_check(number):
    is_prime = False
    for i in range(2, number):
        print(i)
        if number % i == 0:
            print("Ei ole alkuluku")
            break
    else:
        print("On alkuluku")
        is_prime = True

    answer = {
        "Number": number,
        "isPrime": is_prime
    }

#    json_data = json.dumps(answer, default=lambda o: o.__dict__, indent=4)

    return answer


if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)
