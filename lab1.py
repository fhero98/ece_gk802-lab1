import requests  # εισαγωγή της βιβλιοθήκης


url = input("Εισάγετε το URL: ") # Ζητάει από τον χρήστη να εισάγει ένα URL

response = requests.get(url) # Πραγματοποιεί ένα αίτημα HTTP στο URL και την αποθηκευει στην response
headers = response.headers

print("HTTP headers:\n") # Τυπώνει τις headers της απόκρισης HTTP

for header in headers:
    print(header + ": " + headers[header])

server_software = response.headers.get("Server")
if server_software:
    print("Server software:", server_software)
else:
    print("Δεν μπορεί να βρεθεί πληροφορία για το Server software .")

cookies = response.cookies
if cookies:
    print("Η σελίδα χρησιμοποιεί τα παρακάτω cookies:\n")
    for cookie in cookies:
        print("Όνομα:",cookie.name)
        print("Διάρκεια ζωής: \n",cookie.expires)
else:
    print("Η σελίδα δεν χρησιμοποιεί cookies.\n")
