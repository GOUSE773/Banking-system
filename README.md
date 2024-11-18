Banking-system
This is a simple, fully functional banking system built using Python. The project is designed to demonstrate basic banking operations such as creating accounts, making deposits and withdrawals, checking account balances, and viewing transaction histories. It uses object-oriented programming principles for better code organization and scalability.
                                            
                                             ⣀⣤⡤⠤⠴⠒⠚⠛⢿⣿⢻⡟⠛⠛⣛⠓⠒⣒⠒⠒⠒⠒⠒⠦⣤⢤⡀⠀⠀⠀
                                            ⢸⡇⠀⣀⣀⣀⡠⢤⡀⢸⣿⡇⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⡇⣧⠀⠀⠀
                                            ⢸⠀⡞⠉⠀⠀⠀⠈⢹⠀⣿⣇⢹⣸⡋⠉⠉⠉⠉⠉⠉⠉⠉⣿⡜⣿⣷⢹⡄⠀⠀
                                            ⢸⠀⡇⠀⠀⠀⠀⠀⠈⡆⢹⣿⠸⡇⣿⡛⠿⠿⠿⠿⢿⠻⣧⢸⣇⢹⣿⡌⣧⠀⠀
                                            ⢸⠀⡇⠀⠀⠀⠀⠀⠀⢃⠸⣿⡆⣷⢡⣇⣀⡠⠠⠤⠤⣷⢿⡄⣿⠈⣿⣇⢹⠀⠀
                                            ⢸⠀⡇⠀⠀⠀⠀⠀⠀⢸⠀⣿⣧⢸⢸⡼⡀⠀⠀⠀⠀⣸⣾⣇⢹⡇⢻⣿⠸⡄⠀
                                            ⢸⠀⡇⠀⠀⠀⠀⠀⠀⠸⡇⢸⣿⠘⡀⡧⠤⣤⣤⣤⣤⣤⣤⣤⠼⢿⠘⣿⡇⡇⠀
                                            ⢸⠀⡇⠀⠀⠀⠀⠀⠀⠀⣧⠸⣿⡇⡇⢱⣶⣿⣿⢻⣻⣿⣻⣟⣄⢘⡆⣿⣧⢱⠀
                                            ⢸⠀⡇⠀⠀⠀⠀⣤⣤⣤⣿⠀⣿⡇⢁⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢹⣿⢸⠀
                                            ⢸⠀⡇⠀⠀⠀⠀⣿⣲⣿⣿⡀⣿⣿⢸⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠈⣿⢸⡆
                                            ⢸⠀⡇⠀⠀⠀⠀⠙⠛⠙⢹⡇⣿⣿⢸⠀⢨⣿⣿⣟⣿⣿⣻⣿⣿⣿⣿⡆⢻⠈⡇
                                            ⢸⠀⡇⠀⠀⠀⠀⠀⠀⠀⢸⡇⢻⣿⢸⡇⠈⣟⣛⣿⣿⣿⣿⣿⣿⣿⣿⣧⠘⡄⣇
                                            ⢸⠀⡇⠀⠀⠀⠀⠀⠀⠀⢸⡇⣾⣿⣾⡷⠶⠶⢶⣶⣶⣶⣾⣶⣾⡿⠿⠿⠿⡿⣯
                                            ⢸⠀⡇⠀⠀⠀⠀⠀⠀⠀⢸⡇⣿⣿⢸⡇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⡇⣿
                                            ⢸⠓⡗⠲⠦⠤⢤⣄⣀⣀⣸⡇⣿⣿⢸⡇⠀⠀⠈⠉⣉⣉⣉⣁⣀⣀⣀⣠⣤⣧⣿
                                            ⢸⠀⡇⠀⠀⠀⠀⠀⠀⠉⢹⡏⢻⣿⠟⠛⣛⣛⣛⣛⣛⣯⣭⣭⡭⠭⠭⠭⢥⡀⣿
                                            ⢸⠀⣷⣶⣤⣤⣄⡀⠀⠀⢸⡇⢸⣿⢠⡟⠉⣩⣥⣤⣤⣤⣤⣤⣤⠀⠀⠀⠀⡇⣿
                                            ⢸⠀⣿⡇⣴⡄⢹⡇⠀⠀⢸⡇⣼⣿⢸⡇⠀⠿⠿⠿⠛⠛⠛⠛⠋⠀⠀⠀⠀⡇⣿
                                            ⢸⠀⣿⡇⣿⡇⢸⡇⠀⠀⢸⡇⢸⣿⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⣿
                                            ⢸⠀⣿⡇⣿⡇⢸⡇⠀⠀⢸⡇⢸⣿⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⣿
                                            ⢸⠀⣿⡇⠀⠀⢸⡇⠀⠀⢸⡇⢺⣿⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⣿
                                            ⢸⠀⣿⠿⣿⣿⣾⡇⠀⠀⢸⡇⢾⣿⢸⡟⡆⠀⠀⠀⠀⠀⠀⣠⠆⠀⠀⠀⠀⡇⣿
                                            ⢸⠄⢷⣀⡀⠈⠁⠀⠀⠀⢸⡇⣼⣿⢸⡇⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⡇⣿
                                            ⠸⣦⣀⡈⠉⠓⠲⠤⢄⣀⣸⠇⣿⣿⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⣿
                                            ⠀⢠⣿⣿⣿⣶⣦⣄⣀⠀⠀⠀⣽⣿⢸⡇⠀⠀⠀⣀⣀⣀⣤⣤⣤⣶⣶⣶⣿⠛⠋
                                            ⠀⠀⠉⠛⠿⢿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀
                                            ⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠛⠛⠛⠛⠉⠉⠁⠀⠀⠀
💰 Python Banking System: Your Personal Digital Bank 💳
Welcome to the Python Banking System — a simple yet powerful application that turns your terminal into a fully functional digital bank! 🚀 Whether you want to manage your finances, check your account balance, or simply play around with some cool Python code, this project has you covered.

🌟 Key Features:
Open Your Account  : Create a new account in seconds and get a unique account number. No paperwork required! 📝
Deposit & Withdraw : Easily deposit funds or make withdrawals whenever you need cash. 💵💸
Check Your Balance : Need a quick update? Instantly check your current balance with a simple command. 📊
Transaction History: Keep track of all your transactions. Never lose sight of where your money goes! 📜
User-Friendly Menu : Navigate through the options with an intuitive, easy-to-use menu system. No complicated commands — just simple interactions. 🎯

💡 Why This Project?
This project is perfect for beginners looking to dive into Python or for developers who want to brush up on their object-oriented programming skills. With a focus on clean code and essential banking operations, this system is both educational and practical.

📚 Requirements:
Python 3.x installed on your machine.

📈 Future Enhancements:
Adding support for multiple currencies 🌍
Implementing user authentication for enhanced security 🔒
Enabling data persistence with a database 💾

🤝 Contribute:
Found a bug or have a cool feature idea? Feel free to open an issue or submit a pull request. Contributions are always welcome!
