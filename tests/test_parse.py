import parseopera.parse


def test_parse_final_path():
    test_file = "001002-1-001001001.tif"
    output = parseopera.parse.parse_filepath(test_file)
    assert output.well == "B02"
    assert output.channel == 1
    assert output.site ==  1
    assert output.row == 1
    assert output.column == 2
    assert output.filepath == "001002-1-001001001.tif"


def test_parse_full_path():
    test_file = "/root/dir/subdir/001002-1-001001001.tif"
    output = parseopera.parse.parse_filepath(test_file)
    assert output.well == "B02"
    assert output.channel ==  1
    assert output.site == 1
    assert output.row == 1
    assert output.column == 2
    assert output.filepath == "/root/dir/subdir/001002-1-001001001.tif"


