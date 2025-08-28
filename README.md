# MIR-20 Token

<p align="center">
  <img src="/logo.png" alt="MIR-20 Logo" width="120" />
</p>

**MIR-20** is a simple ERC20-like standard designed for the **Mirror Chain**.  
It is a minimal and clean token implementation in Python, focusing only on the essentials:

- Fixed total supply (1,000,000,000 tokens with 6 decimals)  
- No `approve` / `allowance`  
- No `mint` / `burn`  
- No `owner`  

This makes MIR-20 a **lightweight standard** — ideal for learning, simulations, and off-chain prototyping of token logic for the Mirror Chain ecosystem.

---

## Example Usage

```python
# Deploy the token
token = MIR20(deployer="alice")

print("Token:", token.name, token.symbol)
print("Decimals:", token.decimals)
print("Total supply:", token.totalSupply())
print("Alice balance:", token.balanceOf("alice"))

# Alice sends 12.5 MIR to Bob
amt1 = MIR20.to_units(12.5)
token.transfer("alice", "bob", amt1)

print("\nAfter first transfer:")
print("Alice:", MIR20.to_token(token.balanceOf("alice")))
print("Bob:", MIR20.to_token(token.balanceOf("bob")))

# Bob sends 5 MIR to Carol
amt2 = MIR20.to_units(5)
token.transfer("bob", "carol", amt2)

print("\nAfter Bob -> Carol:")
print("Bob:", MIR20.to_token(token.balanceOf("bob")))
print("Carol:", MIR20.to_token(token.balanceOf("carol")))

# Alice airdrops to 3 people in one transaction
pairs = [("dave", MIR20.to_units(100)),
         ("erin", MIR20.to_units(50.5)),
         ("frank", MIR20.to_units(25))]
token.transferMany("alice", pairs)

print("\nAfter Alice airdrop:")
print("Dave:", MIR20.to_token(token.balanceOf("dave")))
print("Erin:", MIR20.to_token(token.balanceOf("erin")))
print("Frank:", MIR20.to_token(token.balanceOf("frank")))

# Show final balances summary
print("\n--- Final Balances ---")
for acc in ["alice", "bob", "carol", "dave", "erin", "frank"]:
    print(acc, "=", MIR20.to_token(token.balanceOf(acc)))
```

---

## Example Output

```
Token: MIR-20 MIR
Decimals: 6
Total supply: 1000000000000000
Alice balance: 1000000000000000

After first transfer:
Alice: 999999987.5
Bob: 12.5

After Bob -> Carol:
Bob: 7.5
Carol: 5.0

After Alice airdrop:
Dave: 100.0
Erin: 50.5
Frank: 25.0

--- Final Balances ---
alice = 999999812.0
bob = 7.5
carol = 5.0
dave = 100.0
erin = 50.5
frank = 25.0
```

---
