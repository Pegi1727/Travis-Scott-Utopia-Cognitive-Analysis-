# Multimodal Mapping Matrix (MMM)
# Simple heuristic mapping of acoustic frequency bands
# to candidate cognitive image schemas.

def map_frequency_to_schema(hz):
    if hz < 100:
        return "FORCE / GROUNDING (Image Schema)"
    elif 100 <= hz < 1000:
        return "PATH / MOVEMENT (Image Schema)"
    elif 1000 <= hz < 5000:
        return "CONTAINER / RESONANCE (Image Schema)"
    else:
        return "VERTICALITY (UP) / CLARITY (Image Schema)"


# Example: high-frequency component in "MY EYES"
frequency = 4000
schema = map_frequency_to_schema(frequency)

print(
    f"Analysis for 'MY EYES' "
    f"({frequency} Hz): {schema}"
)
