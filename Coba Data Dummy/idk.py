import tensorflow as tf

# Definisikan dataset
dataset = tf.data.Dataset.range(10)  # Dataset dengan 10 elemen

# Misalkan kita ingin mengacak dataset sebelum membaginya menjadi batch
BUFFER_SIZE = 5
BATCH_SIZE = 3

# Pengacakan dataset dengan menggunakan buffer
shuffled_dataset = dataset.shuffle(BUFFER_SIZE)

# Bagi dataset menjadi batch-batch kecil
batched_dataset = shuffled_dataset.batch(BATCH_SIZE)

# Iterasi melalui batch-batch dalam dataset
for batch in batched_dataset:
    print("Batch:", batch.numpy())
