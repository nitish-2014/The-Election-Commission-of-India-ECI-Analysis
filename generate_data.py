import pandas as pd
import random

# Parameters
num_rows = 1_000_000
states = ['Tamil Nadu', 'Uttar Pradesh', 'Maharashtra', 'Kerala', 'Bihar', 'West Bengal', 'Rajasthan', 'Karnataka']
constituencies = [f"Constituency_{i}" for i in range(1, 1001)]  # 1000 constituencies
parties = ['BJP', 'INC', 'DMK', 'SP', 'NCP', 'TMC', 'AAP', 'CPI']
years = [2009, 2014, 2019]
phases = [f"Phase {i}" for i in range(1, 8)]

def generate_candidate(party):
    return f"{party}_Candidate_{random.randint(1, 5000)}"

data = []

for _ in range(num_rows):
    state = random.choice(states)
    constituency = random.choice(constituencies)
    year = random.choice(years)
    phase = random.choice(phases)
    party = random.choice(parties)
    candidate = generate_candidate(party)
    votes = random.randint(10000, 1000000)
    vote_percentage = round(random.uniform(5, 60), 2)
    winner = 'Yes' if random.random() < 0.15 else 'No'  # ~15% chance of being winner

    data.append([constituency, state, year, phase, party, candidate, votes, vote_percentage, winner])

# Create DataFrame and save
df = pd.DataFrame(data, columns=[
    'Constituency', 'State', 'Year', 'Phase', 'Party', 'Candidate',
    'Votes', 'Vote_Percentage', 'Winner'
])

df.to_csv("india_election_data_large.csv", index=False)
print("✅ Dataset generated: india_election_data_large.csv")