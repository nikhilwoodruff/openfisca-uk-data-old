def test_synth_downloads():
    from openfisca_data import SynthFRS

    SynthFRS.save()
    assert SynthFRS.file(2018).exists()
