import keyboard
import functions
import moneymaker_config
import accounts
import itertools

print(">>> Press 'page up' to start <<<")
keyboard.wait('page up')

functions.log_message("Started money-maker")

use_thread_kill_shiny = True

pxg_accounts = accounts.pxg_accounts
infinite_accounts = itertools.cycle(pxg_accounts)

for account in infinite_accounts:
    moneymaker_config.login(account["email"], account["senha"], account["imagem"], account["char"])
    moneymaker_config.apply_elixir_mode(use_thread_kill_shiny, account)    
    moneymaker_config.logout()