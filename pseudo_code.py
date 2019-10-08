#!/usr/bin/env python

import numpy as np
import argparse

def pseudo_code():
    basis_config # dictionary
    model_config # dictionary
    target_codec = TargetCodec()

    train_X = []
    train_Y = []
    for xml_fn, match_fn in train_pieces:

        part = load_musicxml(xml_fn)
        unused_part, performance_part, alignment = load_match(match_fn)
    
        # snotes: list of target-relevant snote attributes for all matched snotes
        # notes: list of target-relevant note attributes for all matched notes
        # snote_idx: indices of matched snotes in part
        snote_idx, note_idx = extract_matching_notes(alignment)
        snotes = extract_snote_attributes(part, snote_idx)
        notes = extract_note_attributes(performance_part, note_idx)

        basis = make_basis(part, snote_idx)
        targets = target_codec.encode(snotes, notes)

        train_X.append(basis)
        train_Y.append(targets)
        
    model = train_model(model_config, train_X, train_Y)

    for xml_fn in test_pieces:

        part = load_musicxml(xml_fn)
        basis = make_basis(part, None)
        snotes = extract_snote_attributes(part, None)
        predicted_targets = model.predict(basis)
        predicted_performance_part = target_codec.decode(snotes, predicted_targets)

    
if __name__ == '__main__':
    pass
