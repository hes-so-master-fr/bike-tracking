// Use Signer from @aws-amplify/core
const { Signer } = window.aws_amplify_core;

// AWS Resources
// Cognito:
const identityPoolId = "eu-central-1:66b24b30-0ea8-4021-92dc-7d5b543010c7";

// Amazon Location Service resource names:
const mapName = "Bike-tracker-map";
const placesName = "Bike-tracker-index";

// Extract the region from the Identity Pool ID
AWS.config.region = identityPoolId.split(":")[0];

// Instantiate a Cognito-backed credential provider
const credentials = new AWS.CognitoIdentityCredentials({
  IdentityPoolId: identityPoolId,
});

// Sign requests made by MapLibre GL JS using AWS SigV4:
function transformRequest(url, resourceType) {
  if (resourceType === "Style" && !url.includes("://")) {
    // Resolve to an AWS URL
    url = `https://maps.geo.${AWS.config.region}.amazonaws.com/maps/v0/maps/${url}/style-descriptor`;
  }

  if (url.includes("amazonaws.com")) {
    // Sign AWS requests (with the signature as part of the query string)
    return {
      url: Signer.signUrl(url, {
        access_key: credentials.accessKeyId,
        secret_key: credentials.secretAccessKey,
        session_token: credentials.sessionToken,
      }),
    };
  }

  // If not amazonaws.com, falls to here without signing
  return { url };
}

// Initialize a map
async function initializeMap() {
  // Load credentials and set them up to refresh
  await credentials.getPromise();
  
  // Initialize the map
  const mlglMap = new maplibregl.Map({
    container: "map", // HTML element ID of map element
    
    center: [6.608401, 46.523574], // Initial map centerpoint
    zoom: 16, // Initial map zoom
    style: mapName,
    transformRequest,
  });

  // Add navigation control to the top left of the map
  mlglMap.addControl(new maplibregl.NavigationControl(), "top-left");
  
  return mlglMap;
}

async function main() {
  // Initialize map and AWS SDK for Location Service:
  const map = await initializeMap();
}

main();

