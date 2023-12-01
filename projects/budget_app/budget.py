class Category:
    def __init__(self, cat: str):
        self.name = cat
        self.ledger = []
    
    def __repr__(self):
        rep = f"{self.name:*^30}\n"
        total = f"Total: {self.get_balance():.2f}"
        for item in self.ledger:
            descr = item['description']
            rep += f"{descr[:23]:<23}{item['amount']:>7.2f}\n"

        return f"{rep}{total}"

    def deposit(self, amount: float, description=""):
        dp = {"amount": amount, "description": description}
        self.ledger.append(dp)

    def withdraw(self, amount: float, description=""):
        wd_suc = False
        # Check first if allowed to withdraw by checking balance
        if self.check_funds(amount):
            wd = {"amount": -abs(amount), "description": description}
            self.ledger.append(wd)
            wd_suc = True

        return wd_suc

    def get_balance(self):
        bal = 0
        for li in self.ledger:
            bal = bal + li['amount']
    
        return round(bal, 2)

    def transfer(self, amount, category):
        trn_suc = False
        # withdraw from current category
        if self.check_funds(amount):
            wd_suc = self.withdraw(amount, f"Transfer to {category.name}")
            if wd_suc:
                # deposit to other category
                category.deposit(amount, f"Transfer from {self.name}")
                trn_suc = True

        return trn_suc

    def check_funds(self, amount: float):
        cur_bal = self.get_balance()
        if amount > cur_bal:
            return False
        else:
            return True


food = Category('Food')
entertainment = Category('Entertainment')
business = Category('Business')


food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

print(food)
# print(clothing)



def create_spend_chart(categories):
    def get_perc_val_n10(part, whole):
        per = int((part / whole) * 100)
        if per < 10:
            per = 0
        return round(per / 10) * 10
    # get total spent money for percent calculation
    tot_sp = dict()
    for cat in categories:
        for item in cat.ledger:
            if item['amount'] < 0:
                cur_sp = tot_sp.get(f"{cat.name}", 0)
                tot_sp[f"{cat.name}"] = round(abs(cur_sp) + abs(item['amount']), 2)
    
    grand_tot_sp = sum(tot_sp.values())
    print('TOTAL DIC:', tot_sp)
    print("GRAND_TOTA: ", grand_tot_sp)
    tot_sp_perc = dict()
    for sp in tot_sp:
        perc_val = get_perc_val_n10(tot_sp[sp], grand_tot_sp)
        tot_sp_perc[sp] = tot_sp_perc.get(sp, perc_val)
    
    # Now build percentage barchart
    chart_str = 'Percentage spent by category\n'
    mx_perc = 100
    perc_width = 4 # "100|" is 4
    catlen = len(categories) * 3 # 1 for bar and 2 for space after bar
    cat_keys = tot_sp_perc.keys()
    # Get Category with longest
    def get_mx_char_len():
        cat_chars = list()
        for k in cat_keys:
            cat_chars.append(len(k))
        
        return max(cat_chars)
    
    lngst_cat_letrs = get_mx_char_len()
    cht_wh = catlen + perc_width
    cht_ht = 12 + lngst_cat_letrs # 11 for 0 to 100 + 1 for "-" section

    # Chart "o" bars
    def get_cat_bar_rw(cur_bar_perc):
        rw_str = ''
        for cp in tot_sp_perc:
            if tot_sp_perc[cp] >= cur_bar_perc:
                rw_str += f"o  "
            else:
                rw_str += f"   "

        return f"{rw_str:<{catlen}}"
    
    # Chart Categories characters by rows
    def get_cat_char_rw(cur_rw_cnt):
        char_rw_str = ''
        ltrs_idx = lngst_cat_letrs - (cht_ht - cur_rw_cnt + 1)
        for ky in cat_keys:
            try:
                char_rw_str += f"{ky[ltrs_idx]}  "
            except:
                char_rw_str += "   "

        return char_rw_str

    # Chart Dash separator
    dsh = ""
    c = 0
    while c < cht_wh - 3:
      dsh += "-"
      c += 1
    dashes = f"{dsh:>{cht_wh}}\n"

    # Put it all together to render Barchart
    cntr = 0
    while cntr < cht_ht:
        cntr+= 1
        if mx_perc >= 0:
            perc = f"{mx_perc:>3}| {get_cat_bar_rw(mx_perc)}\n"
            chart_str += f"{perc}"
        if mx_perc == -10:
            chart_str += dashes
        if mx_perc < -10:
            # print("PRINT ALF: ", mx_perc, cntr)
            chars_rw = get_cat_char_rw(cntr)
            sep = '' if cntr == cht_ht else '\n'
            chart_str += f" {chars_rw:>{cht_wh}}{sep}"

        mx_perc -= 10
        # print('mx_perc: ', mx_perc, cntr)

    print(chart_str)
    return chart_str


create_spend_chart([business, food, entertainment])