
import json
import os
from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken

OUTPUT_DIR = Path(__file__).parent
KEY_FILE = OUTPUT_DIR / "demo.key"


def create_or_load_demo_key():
    """Load the local demo key, or create it once."""
    if KEY_FILE.exists():
        return KEY_FILE.read_bytes()

    key = Fernet.generate_key()
    KEY_FILE.write_bytes(key)

    # Restrict permissions where supported; Windows permissions may differ.
    try:
        os.chmod(KEY_FILE, 0o600)
    except OSError:
        pass

    return key


def mask_bank_number(bank_number):
    """Show only the final four digits."""
    return "xxxx" + bank_number[-4:]


def salary_band(salary):
    """Display a pay band instead of an exact salary."""
    if salary < 30000:
        return "Below 30,000"
    if salary < 60000:
        return "30,000-59,999"
    if salary < 100000:
        return "60,000–99,999"
    return "100,000 and above"


def main():
    # Fictional demonstration data only.
    employees = [
        {
            "name": f"Demo Employee {i:02d}",
            "salary": 25000 + (i * 3750),
            "bank_number": f"900000000000{i:04d}",
        }
        for i in range(1, 21)
    ]

    key = create_or_load_demo_key()
    cipher = Fernet(key)

    print("TASK 8: ENCRYPTION AND MASKING DEMO")
    print(f"Fictional employee records: {len(employees)}")
    print()

    # Encrypt salary and bank-style fields using authenticated encryption.
    encrypted_records = []
    for employee in employees:
        encrypted_records.append({
            "name": employee["name"],
            "salary_encrypted": cipher.encrypt(
                str(employee["salary"]).encode("utf-8")
            ).decode("utf-8"),
            "bank_encrypted": cipher.encrypt(
                employee["bank_number"].encode("utf-8")
            ).decode("utf-8"),
        })

    print("1. ENCRYPTED DATA SAMPLE")
    print("Salary ciphertext:", encrypted_records[0]["salary_encrypted"])
    print("Bank ciphertext:  ", encrypted_records[0]["bank_encrypted"])
    print("Ciphertext does not display the original values directly.")
    print()

    # Correct-key decryption test.
    decrypted_salary = cipher.decrypt(
        encrypted_records[0]["salary_encrypted"].encode("utf-8")
    ).decode("utf-8")
    decrypted_bank = cipher.decrypt(
        encrypted_records[0]["bank_encrypted"].encode("utf-8")
    ).decode("utf-8")

    print("2. CORRECT KEY TEST")
    print("Salary decrypted successfully:", decrypted_salary)
    print("Bank number decrypted successfully:", decrypted_bank)
    print()

    # Wrong-key test: Fernet rejects invalid authentication.
    wrong_cipher = Fernet(Fernet.generate_key())
    try:
        wrong_cipher.decrypt(
            encrypted_records[0]["salary_encrypted"].encode("utf-8")
        )
        print("ERROR: Wrong-key test unexpectedly succeeded.")
    except InvalidToken:
        print("3. WRONG KEY TEST: FAILED AS EXPECTED")
        print("The wrong key could not decrypt the protected value.")
    print()

    # Masked display: do not print exact salary or full bank number here.
    print("4. MASKED DISPLAY SAMPLE")
    for employee in employees[:5]:
        print(
            f'{employee["name"]} | '
            f'Salary band: {salary_band(employee["salary"])} | '
            f'Bank: {mask_bank_number(employee["bank_number"])}'
        )

    print()
    print("5. CHECKS")
    print("Exactly 20 fictional records:", len(employees) == 20)
    print(
        "All salary fields encrypted:",
        all("salary_encrypted" in row for row in encrypted_records),
    )
    print(
        "All bank fields encrypted:",
        all("bank_encrypted" in row for row in encrypted_records),
    )
    print()
    print("Demo key stored locally at:", KEY_FILE.name)
    print("Do not commit demo.key to GitHub.")


if __name__ == "__main__":
    main()
