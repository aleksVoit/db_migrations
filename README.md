# db_migrations

# examples of commands for CLI CRUD operations

python3 main.py -a create -m Group -n '22-11'

python3 main.py -a create -m Student -n 'Volodymyr Aleks' -g '22-11'

python3 main.py -a create -m Teacher -n 'Volodymyr Volodymyrovych' 

python3 main.py -a create -m Subject -n 'Python' -t 'Volodymyr Oleksandroych'

python3 main.py -a create -m Mark -b 77 -d 2024-04-24 -s 'Nathan Wilson' -j 'Sport'

python3 main.py -a list -m Student

python3 main.py -a list -m Student -i 51   

python3 main.py -a list -m Student -g 22-11 

python3 main.py -a list -m Subject -t 'Volodymyr Volodymyrovych'

python3 main.py -a list -m Group

python3 main.py -a list -m Mark -s 'Volodymyr Oleksandroych' -j 'Python'

python3 main.py -a list -m Mark -s 'Volodymyr Oleksandroych'

python3 main.py -a update -m Subject -i 19 -n 'New subject' -t 'Volodymyr Volodymyrovych'

python3 main.py -a update -m Group -i 7 -n '22-22'

python3 main.py -a delete -m Subject -i 22

python3 main.py -a delete -m Subject







