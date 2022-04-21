def solution(phone_number):
    # 입력받은 phone_number의 길이를 잰다
    phone = len(phone_number)
    # 인덱스를 활용하여 입력받은 phone_number의 뒷 4자리를 back에 저장
    back = phone_number[-4:]
    # print(back)
    # 뒷 4자리를 제외한 phone_number을 *로 치환 + 뒷 4자리를 더해준다
    return '*'*(phone-4) + back