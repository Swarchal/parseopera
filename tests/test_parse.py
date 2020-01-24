import parseopera.parse


def test_parse_final_path():
    test_file = "001002-1-001001001.tif"
    output = parseopera.parse.parse_filepath(test_file)
    assert output.well == "A02"
    assert output.channel == 1
    assert output.site ==  1
    assert output.row == 1
    assert output.column == 2
    assert output.filepath == "001002-1-001001001.tif"
    test_file2 = "003002-1-001001002.tif"
    output2 = parseopera.parse.parse_filepath(test_file2)
    assert output2.well == "C02"
    assert output2.channel == 2
    assert output2.site ==  1
    assert output2.row == 3
    assert output2.column == 2
    assert output2.filepath == "003002-1-001001002.tif"



def test_parse_full_path():
    test_file = "/root/dir/subdir/001002-1-001001001.tif"
    output = parseopera.parse.parse_filepath(test_file)
    assert output.well == "A02"
    assert output.channel ==  1
    assert output.site == 1
    assert output.row == 1
    assert output.column == 2
    assert output.filepath == "/root/dir/subdir/001002-1-001001001.tif"
    test_file2 = "/root/dir/subdir/003002-1-001001002.tif"
    output2 = parseopera.parse.parse_filepath(test_file2)
    assert output2.well == "C02"
    assert output2.channel == 2
    assert output2.site ==  1
    assert output2.row == 3
    assert output2.column == 2
    assert output2.filepath == "/root/dir/subdir/003002-1-001001002.tif"


