def next_fit_memory_allocation():
    # Maximum number of blocks and processes
    MAX = 25
    
    # Variables to store memory block sizes and process sizes
    frag = [0] * MAX
    b = [0] * MAX
    f = [0] * MAX
    flagn = [0] * MAX

    # Read number of memory blocks and processes
    nb = int(input("Enter the number of blocks: "))
    nf = int(input("Enter the number of Processes: "))
    
    # Read block sizes
    print("\nEnter the size of the blocks:")
    for i in range(nb):
        b[i] = int(input(f"Block {i+1}: "))

    # Read process sizes
    print("Enter the size of the Processes:")
    for i in range(nf):
        f[i] = int(input(f"Process {i+1}: "))

    # Initialize variables for internal fragmentation
    last_allocated_index = -1
    fragi = 0
    fragx = 0

    print("\n\nProcess_No\tProcess_Size\tBlock_No\tBlock_Size\tFragment")

    # Allocate memory to processes using Next Fit algorithm
    for i in range(nf):
        flag = 1  # flag to check if allocation is successful
        start_index = (last_allocated_index + 1) % nb  # Start from the last allocated block

        for j in range(start_index, nb):  # Search from last allocated position onwards
            if f[i] <= b[j]:  # If the process fits in the block
                flagn[j] = 1  # Mark the block as allocated
                print(f"{i+1:<15}{f[i]:<15}{j+1:<15}{b[j]:<15}", end="")
                b[j] -= f[i]  # Reduce the block size after allocation
                fragi += b[j]  # Add the remaining space to internal fragmentation
                print(f"{b[j]:<15}")
                last_allocated_index = j  # Update the last allocated block index
                break
            else:
                flagn[j] = 0  # Mark the block as not allocated
                flag += 1
        
        # If no block found, wrap around and search from the beginning
        if flag > nb:
            for j in range(start_index):
                if f[i] <= b[j]:
                    flagn[j] = 1
                    print(f"{i+1:<15}{f[i]:<15}{j+1:<15}{b[j]:<15}", end="")
                    b[j] -= f[i]
                    fragi += b[j]
                    print(f"{b[j]:<15}")
                    last_allocated_index = j
                    break

        # If no suitable block is found
        if flag > nb:
            print(f"{i+1:<15}{f[i]:<15}{'WAIT...':<15}{'WAIT...':<15}{'WAIT...':<15}")

    # Calculate and print internal fragmentation
    print(f"Internal Fragmentation = {fragi}")

    # Calculate external fragmentation (remaining space in blocks that were not allocated)
    for j in range(nb):
        if flagn[j] != 1:  # If the block is not allocated
            fragx += b[j]  # Add remaining space to external fragmentation

    print(f"External Fragmentation = {fragx}")


# Run the function to simulate Next Fit memory allocation
if __name__ == "__main__":
    next_fit_memory_allocation()
