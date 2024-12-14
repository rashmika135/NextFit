def next_fit_memory_allocation():
    # Variables to store memory block sizes and process sizes
    MAX = 25
    b = [0] * MAX  # Block sizes
    f = [0] * MAX  # Process sizes
    original_b = [0] * MAX  # To store the original block sizes for accurate fragmentation
    flagn = [0] * MAX  # Flags to indicate whether a block is allocated

    # Read number of memory blocks and processes
    nb = int(input("Enter the number of blocks: "))
    nf = int(input("Enter the number of Processes: "))

    # Read block sizes
    print("\nEnter the size of the blocks:")
    for i in range(nb):
        b[i] = int(input(f"Block {i+1}: "))
        original_b[i] = b[i]  # Save original block sizes

    # Read process sizes
    print("Enter the size of the Processes:")
    for i in range(nf):
        f[i] = int(input(f"Process {i+1}: "))

    # Initialize variables for fragmentation
    last_allocated_index = -1  # Track the last allocated block
    fragx = 0  # External fragmentation

    print("\n\nProcess_No\tProcess_Size\tBlock_No\tBlock_Size_Before\tFragment")

    # Allocate memory to processes using Next Fit algorithm
    while True:
        allocated = False  # Flag to indicate if the process was allocated
        start_index = (last_allocated_index + 1) % nb  # Start from the last allocated block

        # First phase: Search from the last allocated index to the end
        for j in range(start_index, nb):
            if f[0] <= b[j]:  # If the process fits in the block
                flagn[j] = 1  # Mark the block as allocated
                print(f"{1:<15}{f[0]:<15}{j+1:<15}{b[j]:<20}", end="")
                b[j] -= f[0]  # Reduce the block size after allocation
                print(f"{b[j]:<15}")
                last_allocated_index = j  # Update the last allocated block
                allocated = True
                break

        # Second phase: Wrap around and search from the start to the last allocated index
        if not allocated:
            for j in range(0, start_index):
                if f[0] <= b[j]:
                    flagn[j] = 1
                    print(f"{1:<15}{f[0]:<15}{j+1:<15}{b[j]:<20}", end="")
                    b[j] -= f[0]
                    print(f"{b[j]:<15}")
                    last_allocated_index = j
                    allocated = True
                    break

        # If no suitable block is found
        if not allocated:
            print(f"{1:<15}{f[0]:<15}{'WAIT...':<15}{'WAIT...':<20}{'WAIT...':<15}")

        # Ask the user if they want to continue or stop
        cont = input("\nDo you want to continue allocation? (yes/no): ").strip().lower()
        if cont != "yes":
            break

        # Move to next process for allocation
        f.pop(0)  # Remove the first process that has been allocated

    # Calculate internal fragmentation
    fragi = sum(original_b[j] - b[j] for j in range(nb) if flagn[j] == 1)

    # Calculate external fragmentation
    for j in range(nb):
        if flagn[j] == 0:  # If the block is not allocated
            fragx += b[j]

    # Display final fragmentation results
    print(f"\nInternal Fragmentation = {fragi}")
    print(f"External Fragmentation = {fragx}")

    # Display final memory status
    print("\nFinal Memory Status:")
    for j in range(nb):
        status = "Allocated" if flagn[j] == 1 else "Free"
        print(f"Block {j+1}: Remaining Size = {b[j]}KB, Status = {status}")


# Run the function to simulate Next Fit memory allocation
if __name__ == "__main__":
    next_fit_memory_allocation()
