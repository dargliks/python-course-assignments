import requests


def download_metadata(pdb_id):
    """
    Download metadata for a PDB entry.
    Returns the JSON dictionary.
    """
    url = f"https://data.rcsb.org/rest/v1/core/entry/{pdb_id}"

    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError("Could not find that PDB entry.")

    return response.json()


def download_pdb_file(pdb_id):
    """
    Download the PDB coordinate file as text.
    """
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"

    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError("Could not download PDB file.")

    return response.text


def analyze_pdb(pdb_text):
    """
    Count atoms, residues, chains and atom types.
    """
    atom_count = 0
    residues = set()
    chains = set()
    atom_types = {}

    for line in pdb_text.splitlines():

        if line.startswith("ATOM"):

            atom_count += 1

            chain = line[21]
            residue_number = line[22:26].strip()

            residues.add((chain, residue_number))
            chains.add(chain)

            element = line[76:78].strip()

            if element == "":
                element = "Unknown"

            atom_types[element] = atom_types.get(element, 0) + 1

    return atom_count, len(residues), len(chains), atom_types


def print_report(metadata, atom_count, residue_count, chain_count, atom_types):

    pdb_id = metadata["rcsb_id"]

    title = metadata["struct"]["title"]

    method = metadata["exptl"][0]["method"]

    print("\n==============================")
    print("Protein Structure Report")
    print("==============================")
    print(f"PDB ID:      {pdb_id}")
    print(f"Title:       {title}")
    print(f"Method:      {method}")

    if "rcsb_entry_info" in metadata:
        info = metadata["rcsb_entry_info"]

        if "resolution_combined" in info:
            resolution = info["resolution_combined"][0]
            print(f"Resolution:  {resolution:.2f} Å")

    print(f"Chains:      {chain_count}")
    print(f"Residues:    {residue_count}")
    print(f"Atoms:       {atom_count}")

    if residue_count > 0:
        average = atom_count / residue_count
        print(f"Atoms/Residue: {average:.2f}")

    print("\nAtom composition:")

    for element in sorted(atom_types):
        print(f"  {element:>2}: {atom_types[element]}")

    print("==============================")


def main():

    pdb_id = input("Enter a PDB ID: ").upper().strip()

    try:
        metadata = download_metadata(pdb_id)

        pdb_text = download_pdb_file(pdb_id)

        atom_count, residue_count, chain_count, atom_types = analyze_pdb(pdb_text)

        print_report(
            metadata,
            atom_count,
            residue_count,
            chain_count,
            atom_types,
        )

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()