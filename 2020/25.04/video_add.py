def skleyka_video(files=[], out_name="Output.mp4"):
    out = []
    print("Collecting videos...")
    for file in files:
        with open(file, "rb") as f:
            out.extend(f.readlines())
    print("Making video...")
    with open(out_name, "wb") as f:
        for i in out:
            f.write(i)
    print("Done")


skleyka_video(["aa.mp4", "bb.mp4"])