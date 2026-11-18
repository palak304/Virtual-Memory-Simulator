
def fifo(pages, frames):
    memory = []
    history = []
    hits = 0
    faults = 0

    for page in pages:
        if page in memory:
            hits += 1
            status = "Hit"
        else:
            faults += 1
            status = "Fault"

            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)

        history.append({
            "Page": page,
            "Frames": memory.copy(),
            "Status": status
        })

    return history, hits, faults


def lru(pages, frames):
    memory = []
    history = []
    hits = 0
    faults = 0

    for page in pages:
        if page in memory:
            hits += 1
            status = "Hit"
            memory.remove(page)
            memory.append(page)
        else:
            faults += 1
            status = "Fault"

            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)

        history.append({
            "Page": page,
            "Frames": memory.copy(),
            "Status": status
        })

    return history, hits, faults


def optimal(pages, frames):
    memory = []
    history = []
    hits = 0
    faults = 0

    for i, page in enumerate(pages):
        if page in memory:
            hits += 1
            status = "Hit"
        else:
            faults += 1
            status = "Fault"

            if len(memory) < frames:
                memory.append(page)
            else:
                future = pages[i + 1:]

                distances = [
                    future.index(p) if p in future else float('inf')
                    for p in memory
                ]

                replace_index = distances.index(max(distances))
                memory[replace_index] = page

        history.append({
            "Page": page,
            "Frames": memory.copy(),
            "Status": status
        })

    return history, hits, faults
