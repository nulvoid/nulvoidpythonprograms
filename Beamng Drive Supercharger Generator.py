while True: #gear ratio
    gear_ratio = input("Enter gear ratio: ")
    if gear_ratio.lower() == "help":
        print("For best results, enter a number between 1.0 and 4.0 for the supercharger gear ratio.")
    elif 1 < float(gear_ratio) < 4:
        break
    else:
        print("Invalid gear ratio. Please enter a value between 1.0 and 4.0.")
while True: #clutch engage rpm
    clutch_engage_rpm = input("Enter clutch engage RPM: ")
    if clutch_engage_rpm.lower() == "help":
        print("RPM where the supercharger clutch engages. Most of the time, you want 0. Don't enter an RPM higher than what the engine will run at, the supercharger will never engage.")
    elif float(clutch_engage_rpm) >= 0:
        break
    else:
        print("Invalid RPM. Please enter a value of at least 0.")
while True: #pressure rate psi
    pressure_rate_psi = input("Enter pressure rate PSI: ")
    if pressure_rate_psi.lower() == "help":
        print("How fast the supercharger can build pressure, does not effect max pressure. For best results enter a value between 50 and 500.")
    elif 1 < float(pressure_rate_psi) < 1000:
        break
    else:
        print("Invalid pressure rate. Please enter a value between 1 and 1000.")
while True: #pressure psi  per 1k rpm
    pressure_psi_per_1k_rpm = input("Enter pressure PSI per 1k RPM: ")
    if pressure_psi_per_1k_rpm.lower() == "help":
        print("How much pressure the supercharger generates per it's RPM. For best results, enter a value between 1.2 and 4.")
    elif 0.1 < float(pressure_psi_per_1k_rpm) < 5:
        break
    else:
        print("Invalid pressure PSI. Please enter a value between 0.1 and 5.")
while True: #crank loss per 1k rpm
    crank_loss_per_1k_rpm = input("Enter crank loss per 1k RPM: ")
    if crank_loss_per_1k_rpm.lower() == "help":
        print("How much power is needed to spin the supercharger for every 1000 RPM. For best results, enter a value between 1 and 10.")
    elif 1 < float(crank_loss_per_1k_rpm) < 20:
        break
    else:
        print("Invalid crank loss. Please enter a value between 1 and 20.")
while True: #supercharger type
    supertype = input("Enter supercharger type: ").lower()
    if supertype == "help":
        print("Valid options for supercharger type include roots, screws, and centrifugal.")
    elif supertype == "roots" or supertype == "screws" or supertype == "centrifugal":
        break
    else:
        print("Invalid supercharger type. Please enter a valid supercharger type.")
if supertype == "roots": #twisted lobes?
    while True:
        twistedlobes = input("Twisted lobes? ").lower()
        if twistedlobes == "help":
            print("Whether or not the lobes are twisted. Answer with yes or no. Twisted lobes make more power.")
        elif twistedlobes == "yes":
            twistedlobes = "true"
            break
        elif twistedlobes == "no":
            twistedlobes = "false"
            break
        else:
            print("Invalid option. Please enter yes or no.")
while True: #number of lobes
    lobes = input("Enter number of lobes: ")
    if lobes.lower() == "help":
        print("Number of lobes inside the supercharger. Enter a value between 1 and 4.")
    elif 1 < float(lobes) < 4:
        break
    else:
        print("Invalid number of lobes. Please enter a value between 1 and 4.")
while True: #whine volume per 10k rpm
    whine_volume_per_10k_rpm = input("Enter whine volume per 10k RPM: ")
    if whine_volume_per_10k_rpm.lower() == "help":
        print("Increases volume of the supercharger whine per 10000 RPM. For best results, enter a value between 0.01 and 0.25.")
    elif 0.01 < float(whine_volume_per_10k_rpm) < 0.5:
        break
    else:
        print("Invalid whine volume. Please enter a value between 0.01 and 0.5.")
while True: #whine pitch per 10k rpm
    whine_pitch_per_10k_rpm = input("Enter whine pitch per 10k RPM: ")
    if whine_pitch_per_10k_rpm.lower() == "help":
        print("Increases pitch of the supercharger whine per 10000 RPM. For best results, enter a value between 0.1 and 1.5.")
    elif 0.05 < float(whine_pitch_per_10k_rpm) < 2:
        break
    else:
        print("Invalid whine pitch. Please enter a value between 0.05 and 1.5.")

#Define the text to be output
output_text = f'''
"supercharger": {{
    "gearRatio": {gear_ratio},
    "clutchEngageRPM": {clutch_engage_rpm},
    "pressureRatePSI": {pressure_rate_psi},
    "pressurePSIPer1kRPM": {pressure_psi_per_1k_rpm},
    "crankLossPer1kRPM": {crank_loss_per_1k_rpm},
    "type": {supertype},
    "lobes": {lobes},
    "twistedLobes": {twistedlobes},
    "whineLoopEvent": "event:>Vehicle>Forced_Induction>Supercharger_03>supercharger",
    "whineVolumePerPSI": {whine_volume_per_10k_rpm},
    "whinePitchPer10kRPM": {whine_pitch_per_10k_rpm},
    "boostController": [
        //throttle in %, factor
        [0, 0.2],
        [100, 1],
    ],
}},
'''

with open("output.txt", "w") as file:
    file.write(output_text)
print("Output has been written to 'output.txt' file:")
print(output_text)
input("Press enter to exit program")
