import { Campaign } from "@/types/campaign";

// API base URL - change this to your Railway backend URL after deployment
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

/**
 * Fetch all campaigns or filter by status
 */
export async function fetchCampaigns(status?: string): Promise<Campaign[]> {
  try {
    const url = status && status !== "All"
      ? `${API_BASE_URL}/campaigns?status=${status}`
      : `${API_BASE_URL}/campaigns`;

    const response = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching campaigns:", error);
    throw new Error("Failed to fetch campaigns. Please check your API connection.");
  }
}

/**
 * Fetch a single campaign by ID
 */
export async function fetchCampaignById(id: number): Promise<Campaign> {
  try {
    const response = await fetch(`${API_BASE_URL}/campaigns/${id}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching campaign:", error);
    throw new Error("Failed to fetch campaign details.");
  }
}