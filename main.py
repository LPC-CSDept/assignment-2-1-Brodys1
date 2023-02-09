def main():
    ##################################################
    # Comlete your code here
    men = int(input('Number of male indentifying students : '))
    women = int(input('Number of female indentifying students : '))
    students = int(women + men)
    per_males = (men/students)*100
    per_females = (women/students)*100
    print(f'\nThe total number of students:\t\t{students}\
        \nThe number of males and females:\t {men}\t {women}\
        \nThe percentage of males and females:\t {per_males:.2f}\t {per_females:.2f}')
    ##################################################
    pass


if __name__ == '__main__':
    main()
