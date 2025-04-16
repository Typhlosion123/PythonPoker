import pandas as pd
def poker_ledger(buy_ins, buy_outs):
    results = {}
    for player in buy_ins.keys():
        buy_in = buy_ins[player]
        buy_out = buy_outs[player]
        net_result = buy_out - buy_in
        results[player] = net_result
    winners = []
    losers = []
    for player, net in results.items():
        if net > 0:
            winners.append(player)
        elif net < 0:
            losers.append(player)
    winners.sort(key=lambda player: results[player], reverse=True)  # Largest winner first
    losers.sort(key=lambda player: results[player])
    print("Poker Ledger:")
    for loser in losers:
        amount_owed = abs(results[loser])

        for winner in winners:
            if amount_owed == 0:
                break
            winner_net = results[winner]
            if winner_net == 0:
                continue
            payment = min(amount_owed, winner_net)
            print(f"{loser} owes {winner} ${round(payment)}")
            amount_owed -= payment
            results[winner] -= payment
def load_data_from_excel(file_path):
    df = pd.read_excel(file_path, header=None)
    buy_in = {row[0]: row[1] for row in df.itertuples(index=False)}
    buy_out = {row[0]: row[2] for row in df.itertuples(index=False)}

    return buy_in, buy_out

file_path = r'C:\Users\Admin\Downloads\Poker 10_7.xlsx'
buy_in, buy_out = load_data_from_excel(file_path)
poker_ledger(buy_in, buy_out)