// Savorly shared API types (v0.1)

export interface GenerateRequest {
  ingredients: string[];
  dietary_flags?: Record<string, boolean>;
}

export interface Recipe {
  id: string;
  title: string;
  ingredients: string[];
  steps_md: string;
}

export interface GenerateResponse {
  recipes: Recipe[];
}
