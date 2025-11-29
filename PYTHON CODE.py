
import boto3

def polly_text_to_speech(text, output_file):
    try:
        # Create a Polly client
        polly = boto3.client(
            "polly",
            region_name="ap-south-1"   # India region (choose your own)
        )

        # Request setup
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId="Joanna"   # Aditi (Indian English), Raveena (Hindi), Matthew, etc.
        )

        # Read audio stream and save it
        if "AudioStream" in response:
            with open(output_file, "wb") as f:
                f.write(response["AudioStream"].read())
            print(f"Speech generated successfully → {output_file}")
        else:
            print("No audio stream received.")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    polly_text_to_speech(
        text="Hello swapna! This is your Amazon Polly Python project.",
        output_file="output.mp3"
    )
