"""
Multimodal Mapping Matrix (MMM)
--------------------------------
A heuristic analytical framework for relating acoustic
features to candidate cognitive image schemas.

Important:
This script does NOT claim that a specific frequency
deterministically activates a specific image schema.
Rather, frequency bands are treated as acoustic cues
that may support candidate schema interpretations
within a multimodal analytical context.
"""


def infer_candidate_schema(hz):
    """
    Infer a candidate cognitive image schema from
    an acoustic frequency band.

    Parameters
    ----------
    hz : float
        Acoustic frequency in Hertz.

    Returns
    -------
    str
        Candidate image-schema interpretation.
    """

    if hz < 100:
        return "FORCE / GROUNDING"

    elif hz < 1000:
        return "PATH / MOVEMENT"

    elif hz < 3000:
        return "CONTAINER / RESONANCE"

    else:
        return "VERTICALITY (UP) / CLARITY"


def analyze_frequency(track, hz):
    """
    Apply the MMM heuristic to an acoustic feature
    from a focal track.
    """

    schema = infer_candidate_schema(hz)

    print(f"Track: {track}")
    print(f"Frequency: {hz} Hz")
    print(f"Candidate Image Schema: {schema}")
    print("-" * 50)

    return schema


# --------------------------------------------------
# Example application: "MY EYES"
# --------------------------------------------------

frequency = 4000

analyze_frequency(
    track="MY EYES",
    hz=frequency
)
