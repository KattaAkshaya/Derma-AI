import numpy as np
import cv2

def analyze_skin_opencv(image):
    try:
        # Convert image to OpenCV format
        image = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Resize for processing
        resized = cv2.resize(image, (300, 300))

        # Convert to HSV for skin tone analysis
        hsv = cv2.cvtColor(resized, cv2.COLOR_RGB2HSV)
        avg_color = np.mean(hsv, axis=(0, 1))

        # Determine skin tone based on brightness
        h, s, v = avg_color
        if v > 200:
            skin_tone = "Light"
        elif 100 < v <= 200:
            skin_tone = "Medium"
        else:
            skin_tone = "Dark"

        # Detect redness (blemishes/acne)
        lower_red = np.array([0, 50, 50])
        upper_red = np.array([10, 255, 255])
        mask_red = cv2.inRange(hsv, lower_red, upper_red)
        blemish_percentage = np.sum(mask_red > 0) / (300 * 300) * 100
        skin_condition = "Blemishes/Redness Detected" if blemish_percentage > 5 else "Smooth Skin Detected"

        # Detect oiliness (high shine areas)
        brightness = np.mean(v)
        if brightness > 180:
            oiliness = "High Shine Detected (Possibly Oily Skin)"
        elif brightness > 140:
            oiliness = "Normal Shine"
        else:
            oiliness = "Matte Appearance (Possibly Dry Skin)"

        # Detect dryness (patchy low-brightness regions)
        lower_dry = np.array([0, 0, 150])
        upper_dry = np.array([255, 50, 255])
        mask_dry = cv2.inRange(hsv, lower_dry, upper_dry)
        dryness_percentage = np.sum(mask_dry > 0) / (300 * 300) * 100
        dryness = "Dry Patches Detected" if dryness_percentage > 3 else "No Significant Dryness"

        # Detect hyperpigmentation (dark spots)
        lower_dark = np.array([0, 0, 0])
        upper_dark = np.array([180, 255, 80])
        mask_dark = cv2.inRange(hsv, lower_dark, upper_dark)
        dark_spot_percentage = np.sum(mask_dark > 0) / (300 * 300) * 100
        hyperpigmentation = "Dark Spots/Hyperpigmentation Detected" if dark_spot_percentage > 2 else "Even Skin Tone"

        # Detect fine lines/wrinkles (using edge detection)
        gray = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(gray, 30, 100)
        wrinkle_percentage = np.sum(edges > 0) / (300 * 300) * 100
        wrinkles = "Fine Lines/Wrinkles Detected" if wrinkle_percentage > 3 else "No Significant Wrinkles"

        # Detect large pores (High contrast areas)
        blur = cv2.GaussianBlur(gray, (7, 7), 0)
        detail = cv2.absdiff(gray, blur)
        pores_percentage = np.sum(detail > 20) / (300 * 300) * 100
        pores = "Large Pores Detected" if pores_percentage > 5 else "Normal Pore Size"

        # Detect uneven skin texture (rough patches)
        texture = "Uneven Skin Texture Detected" if pores_percentage > 7 else "Smooth Skin Texture"

        # Detect dark circles (lower brightness under eyes)
        eye_region = gray[180:220, 100:200]  # Approximate region for eyes
        eye_brightness = np.mean(eye_region)
        dark_circles = "Dark Circles Detected" if eye_brightness < 50 else "No Dark Circles"

        # Detect UV/sun damage (yellowish spots)
        lower_uv = np.array([10, 50, 50])
        upper_uv = np.array([30, 255, 255])
        mask_uv = cv2.inRange(hsv, lower_uv, upper_uv)
        uv_damage_percentage = np.sum(mask_uv > 0) / (300 * 300) * 100
        uv_damage = "Signs of Sun Damage Detected" if uv_damage_percentage > 2 else "No Significant UV Damage"

        return {
            "skin_tone": skin_tone,
            "condition": skin_condition,
            "blemish_percentage": blemish_percentage,
            "oiliness": oiliness,
            "dryness": dryness,
            "hyperpigmentation": hyperpigmentation,
            "wrinkles": wrinkles,
            "pores": pores,
            "texture": texture,
            "dark_circles": dark_circles,
            "uv_damage": uv_damage
        }

    except Exception as e:
        return {"error": str(e)}
