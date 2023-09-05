import TMPower
import TMModulo
import TMAddition
import TMSubstraction
import TMMultiplication
import TMLogarithm
import TMFactorial
import TMDivision

if __name__ == '__main__':
    while True:
        print('TURING MACHINE SIMULATOR')
        print('1. Turing Machine Addition')
        print('2. Turing Machine Subtraction')
        print('3. Turing Machine Multiplication')
        print('4. Turing Machine Division')
        print('5. Turing Machine Factorial')
        print('6. Turing Machine Modulo')
        print('7. Turing Machine Power')
        print('8. Turing Machine Logarithm')
        print('9. Exit')
        a = int(input('Select Option : '))
        if a == 1:
            TMAddition.start_machine()
            print()
        if a == 2:
            TMSubstraction.start_machine()
            print()
        if a == 3:
            TMMultiplication.start_machine()
            print()
        if a == 4:
            TMDivision.start_machine()
            print()
        if a == 5:
            TMFactorial.start_machine()
            print()
        if a == 6:
            TMModulo.start_machine()
            print()
        if a == 7:
            TMPower.start_machine()
            print()
        if a == 8:
            TMLogarithm.start_machine()
            print()
        if a == 9:
            break
        else:
            print("Masukkan pilihan yang tersedia")
            print()
