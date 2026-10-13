import numpy as np

np.random.seed(42)
puppies = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

p = puppies.mean()
print("Mean",p)
print("Standard deviation", puppies.std())
print("Variance", puppies.var())

np.random.choice(puppies, size=(1,5), replace=True)
np.random.choice(puppies, size=(1,5), replace=True).mean()

print("\nSampling Distribution with size 5 \n") 
sample_props = []
for i in range(10000):
    sample = np.random.choice(puppies, size=(1,5), replace=True)
    sample_props.append(sample.mean())
sample_props = np.array(sample_props)

sm = sample_props.mean()
print("Mean", sample_props.mean())
print("Standard deviation", sample_props.std())
print("Variance", sample_props.var())

print("\nSampling Distribution with size 20 \n")

twenty_sample_props = []
for i in range(10000):
    sample = np.random.choice(puppies, 20, replace=True)
    twenty_sample_props.append(sample.mean())  # Call the mean() method here

# Convert the list to a NumPy array
twenty_sample_props = np.array(twenty_sample_props)

print(" New Mean", twenty_sample_props.mean())
print(" New Standard deviation", twenty_sample_props.std())
print(" New Variance", twenty_sample_props.var())