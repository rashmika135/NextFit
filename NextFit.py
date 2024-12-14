def next_fit_memory_allocation():
    # Variables to store memory block sizes and process sizes
    MAX = 25
    b = [0] * MAX  
    f = [0] * MAX  
    original_b = [0] * MAX  
    flagn = [0] * MAX 

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

    
    last_allocated_index = -1  # Track the last allocated block

    print("\n\nProcess_No\tProcess_Size\tBlock_No\tBlock_Size_Before\tFragment")

    # Allocate memory to processes using Next Fit algorithm
    for i in range(nf):
        allocated = False  
        start_index = (last_allocated_index + 1) % nb 

        #search from the last allocated index to the end
        for j in range(start_index, nb):
            if f[i] <= b[j]: 
                flagn[j] = 1  
                print(f"{i+1:<15}{f[i]:<15}{j+1:<15}{b[j]:<20}", end="")  
                b[j] -= f[i]  
                print(f"{b[j]:<15}")
                last_allocated_index = j 
                allocated = True
                break

        #Wrap around and search from the start to the last allocated index
        if not allocated:
            for j in range(0, start_index):
                if f[i] <= b[j]:
                    flagn[j] = 1
                    print(f"{i+1:<15}{f[i]:<15}{j+1:<15}{b[j]:<20}", end="")
                    b[j] -= f[i]
                    print(f"{b[j]:<15}")
                    last_allocated_index = j
                    allocated = True
                    break

        # If no suitable block is found
        if not allocated:
            print(f"{i+1:<15}{f[i]:<15}{'WAIT...':<15}{'WAIT...':<20}{'WAIT...':<15}")

    # Calculate and display internal fragmentation 
    fragi = 0  
    print("\nInternal Fragmentation Breakdown:")
    for j in range(nb):
        if flagn[j] == 1: 
            fragment = original_b[j] - (original_b[j] - b[j])
            fragi += fragment
            print(f"Block {j+1}: Original Size = {original_b[j]}, " +
                  f"Allocated Size = {original_b[j] - b[j]}, " +
                  f"Fragment = {fragment}")

    # Calculate external fragmentation
    fragx = 0  
    for j in range(nb):
        if flagn[j] == 0:  
            fragx += b[j]  

    # Display final fragmentation results
    print(f"\nInternal Fragmentation = {fragi}KB")
    print(f"External Fragmentation = {fragx}KB")

    # Display final memory status
    print("\nFinal Memory Status:")
    for j in range(nb):
        status = "Allocated" if flagn[j] == 1 else "Free"
        print(f"Block {j+1}: Remaining Size = {b[j]}KB, Status = {status}")

# Run the function to simulate Next Fit memory allocation
if __name__ == "__main__":
    next_fit_memory_allocation()